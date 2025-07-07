"""
Dependencies for API routes
"""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import ALGORITHM, SECRET_KEY

# Import từ app structure
from app.core.database import get_db
from app.models.user import Users

# OAuth2 scheme for token authentication
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


# =============================================================================
# AUTHENTICATION DEPENDENCIES
# =============================================================================


async def get_current_user(
    token: Annotated[str, Depends(oauth2_bearer)],
    db: Annotated[Session, Depends(get_db)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        user_role: str = payload.get("role")

        if username is None or user_id is None or user_role is None:
            raise credentials_exception
        return {"username": username, "id": user_id, "role": user_role}
    except JWTError:
        raise credentials_exception


async def get_current_active_user(
    current_user: Annotated[Users, Depends(get_current_user)],
):
    """
    Check if current user is active
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )
    return current_user
