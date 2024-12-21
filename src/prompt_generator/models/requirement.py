from pydantic import BaseModel, Field
from typing import List, Optional


class Requirement(BaseModel):
    """要件定義を表現するモデル"""

    title: str = Field(..., description="要件の題名")
    description: str = Field(..., description="要件の詳細な説明")
    constraints: List[str] = Field(default_factory=list, description="制約条件のリスト")
    goals: List[str] = Field(default_factory=list, description="達成目標のリスト")
    context: Optional[str] = Field(None, description="追加のコンテキスト情報")
