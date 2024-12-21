from typing import Dict, Any
from ..models.requirement import Requirement
from ..models.prompt import Prompt

def validate_requirement(data: Dict[str, Any]) -> bool:
    """
    要件定義データのバリデーションを行う

    Args:
        data: バリデーション対象のデータ

    Returns:
        bool: バリデーション結果
    """
    try:
        Requirement(**data)
        return True
    except Exception:
        return False

def validate_prompt(data: Dict[str, Any]) -> bool:
    """
    生成されたプロンプトのバリデーションを行う

    Args:
        data: バリデーション対象のデータ

    Returns:
        bool: バリデーション結果
    """
    try:
        Prompt(**data)
        return True
    except Exception:
        return False
