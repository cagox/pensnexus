from datetime import datetime, timezone
from sqlalchemy import ForeignKey, BigInteger, select
from sqlalchemy.orm import Mapped, Session, mapped_column
from typing import Optional
import pyotp

from ..db.types import Base, bigint_pk, created_at_dt, nullable_time_stamp, updated_at_dt, nullable_text_content, unique_user_data

from ..crypto.passwords import hash_password, verify_password

class Profile(Base):
	__tablename__ = "profiles"
	#
	id: Mapped[bigint_pk]
	created_at: Mapped[created_at_dt]
	last_updated: Mapped[updated_at_dt]
	deactivated_at: Mapped[nullable_time_stamp] # None if active
	user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
	display_name: Mapped[unique_user_data] 
	bio: Mapped[nullable_text_content] # None if not set
	#TODO : Add social media links, profile picture, etc.
	#
	@classmethod
	def create(cls, user_id: int, display_name: str, bio: Optional[str] = None) -> "Profile":
		return cls(
			user_id = user_id,
			display_name = display_name,
			bio=bio,
		)
	#
	#
	@classmethod
	def get_by_id(cls, session: Session, profile_id: int) -> Optional["Profile"]:
		return session.get(cls, profile_id)
	#
	#
	def commit_to_db(self, session: Session) -> "Profile":
		session.add(self)
		session.commit()
		session.refresh(self)
		return self
	#
	#
	@property
	def is_deactivated(self) -> bool:
		return self.deactivated_at is not None

	



