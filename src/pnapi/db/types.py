from ..config import settings
import uuid
import uuid6
from datetime import datetime
from typing import Annotated, Optional
from sqlalchemy import String, BigInteger, DateTime, Boolean, Text, UUID, func, false
from sqlalchemy.orm import DeclarativeBase, mapped_column


# --- Custom Object ID Type using UUID ---
# UUIDs as primary keys can be useful for distributed systems.
def generate_node_uuid() -> uuid.UUID:
	"""
	Generates a UUIDv6 based on the node_id from settings.

	Returns:
		uuid.UUID: A UUIDv6 object.
	"""
	return uuid6.uuid6(node=settings.node_id)
uuid_pk = Annotated[uuid.UUID, mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_node_uuid)]



# --- Reusable Custom Types ---
# BigInt primary key
bigint_pk = Annotated[int, mapped_column(BigInteger, primary_key=True, autoincrement=True)]

# Standard indexed email
unique_user_data = Annotated[str, mapped_column(String(255), unique=True, index=True, nullable=False)]

# Auto-populating timestamp
created_at_dt = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=func.now())]

# Auto-updating timestamp
updated_at_dt = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())]

# General purpose timestamp
nullable_time_stamp = Annotated[Optional[datetime], mapped_column(DateTime(timezone=True), nullable=True, default=None)]

# usable for boolean flags with default False, such as is_admin
default_false_bool = Annotated[bool, mapped_column(Boolean, default=False, server_default=false(), nullable=False)]

# Free Text fields
text_content = Annotated[str, mapped_column(Text, nullable=False)]
nullable_text_content = Annotated[Optional[str], mapped_column(Text, nullable=True, default=None)]


# The base for database classes
class Base(DeclarativeBase):
	pass
