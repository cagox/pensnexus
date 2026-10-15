from sqlalchemy import String, select, datetime, timezone
from sqlalchemy.orm import Mapped, Session, mapped_column
from typing import Optional
import pyotp

from ..db.types import Base, bigint_pk, user_email, created_at_dt, nullable_time_stamp, updated_at_dt

from ..crypto.passwords import hash_password, verify_password

class User(Base):
	__tablename__ = "users"
	#
	id: Mapped[bigint_pk]
	email: Mapped[user_email]
	created_at: Mapped[created_at_dt]
	last_updated: Mapped[updated_at_dt]
	date_verified: Mapped[nullable_time_stamp] # None if email not verified
	deactivated_at: Mapped[nullable_time_stamp] # None if active
	otp_verified_at: Mapped[nullable_time_stamp] # None if OTP has never successfully been used
	password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
	otp_secret: Mapped[str] = mapped_column(String(32), nullable=False)
	#
	@classmethod
	def create(cls, email: str, password: str) -> "User":
		return cls(
			email = email.strip().lower(),
			password_hash = hash_password(password),
			otp_secret = pyotp.random_base32(),
		)
	#
	#
	@classmethod
	def get_by_email(cls, session: Session, email: str) -> Optional["User"]:
		statement = select(cls).where(cls.email == email.strip().lower())
		return session.scalar(statement)
	#
	#
	@classmethod
	def get_by_id(cls, session: Session, user_id: int) -> Optional["User"]:
		return session.get(cls, user_id)
	#
	#	
	def verify_password(self, password_string: str) -> bool:
		return verify_password(self.password_hash, password_string)
	#
	#
	def commit_to_db(self, session: Session) -> "User":
		session.add(self)
		session.commit()
		session.refresh(self)
		return self
	#
	#
	def verify_otp(self, token: str, mark_verified: bool = False) -> bool:
		"""Verifies a 6-digit TOTP token against the stored secret."""
		totp = pyotp.TOTP(self.otp_secret)
		is_valid = totp.verify(token)
		if is_valid and mark_verified:
			self.otp_verified_at = datetime.now(timezone.utc)
		return is_valid
	#
	#
	@property
	def is_deactivated(self) -> bool:
		return self.deactivated_at is not None

	



