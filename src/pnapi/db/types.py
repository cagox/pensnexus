from datetime import datetime
from typing import Annotated, Optional
from sqlalchemy import String, BigInteger, DateTime, Boolean, func, false
from sqlalchemy.orm import DeclarativeBase, mapped_column


# --- Reusable Custom Types ---
# BigInt primary key
bigint_pk = Annotated[int, mapped_column(BigInteger, primary_key=True, autoincrement=True)]

# Standard indexed email
user_email = Annotated[str, mapped_column(String(255), unique=True, index=True, nullable=False)]

# Auto-populating timestamp
created_at_dt = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=func.now())]

# Auto-updating timestamp
updated_at_dt = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())]

# General purpose timestamp
nullable_time_stamp = Annotated[Optional[datetime], mapped_column(DateTime(timezone=True), nullable=True, default=None)]

# Deletable Object
default_false_bool = Annotated[bool, mapped_column(Boolean, default=False, server_default=false(), nullable=False)]

# The base for database classes
class Base(DeclarativeBase):
	pass
