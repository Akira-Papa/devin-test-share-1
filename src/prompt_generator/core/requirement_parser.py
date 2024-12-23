from typing import Dict, Any
from ..models.requirement import Requirement


class RequirementParser:
    """要件定義をパースし、構造化されたデータに変換するクラス"""

    @staticmethod
    def parse(raw_requirement: Dict[str, Any]) -> Requirement:
        """
        生の要件定義データをRequirementモデルに変換する

        Args:
            raw_requirement: 要件定義の生データ

        Returns:
            Requirement: パース済みの要件定義
        """
        return Requirement(**raw_requirement)
