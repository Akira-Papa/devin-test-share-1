from pydantic import BaseModel, Field
from typing import List, Optional

class Prompt(BaseModel):
    """生成されたシステムプロンプトを表現するモデル"""
    system_prompt: str = Field(..., description="生成されたシステムプロンプト")
    context: str = Field(..., description="プロンプトのコンテキスト")
    constraints: List[str] = Field(default_factory=list, description="プロンプトの制約条件")
    capabilities: List[str] = Field(default_factory=list, description="AIエージェントの機能と制限")
    metadata: Optional[dict] = Field(default_factory=dict, description="追加のメタデータ")
