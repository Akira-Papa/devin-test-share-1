from typing import Dict, Any, List
from ..models.requirement import Requirement
from ..models.prompt import Prompt


class PromptGenerator:
    """要件定義からシステムプロンプトを生成するクラス"""

    def generate(self, requirement: Requirement) -> Prompt:
        """
        要件定義からシステムプロンプトを生成する

        Args:
            requirement: パース済みの要件定義

        Returns:
            Prompt: 生成されたシステムプロンプト
        """
        # システムプロンプトのテキストを生成
        system_prompt = self._create_system_prompt(requirement)

        # 制約条件のリストを取得
        constraints = requirement.constraints.copy()

        # 機能リストを導出
        capabilities = self._derive_capabilities(requirement)

        # メタデータを準備
        metadata: Dict[str, Any] = {"source_requirement": requirement.title}

        # プロンプトオブジェクトを生成して返す
        return Prompt(
            system_prompt=system_prompt,
            context=requirement.description,
            constraints=constraints,
            capabilities=capabilities,
            metadata=metadata,
        )

    def _create_system_prompt(self, requirement: Requirement) -> str:
        """システムプロンプトのテキストを生成する"""
        prompt_parts = [
            f"目的: {requirement.title}",
            f"コンテキスト: {requirement.description}",
        ]

        if requirement.constraints:
            prompt_parts.append("制約条件:")
            prompt_parts.extend(
                [f"- {constraint}" for constraint in requirement.constraints]
            )

        if requirement.goals:
            prompt_parts.append("達成目標:")
            prompt_parts.extend([f"- {goal}" for goal in requirement.goals])

        return "\n".join(prompt_parts)

    def _derive_capabilities(self, requirement: Requirement) -> List[str]:
        """要件から必要な機能を導出する"""
        # 基本的な機能セット
        capabilities = [
            "要件の理解と解釈",
            "コンテキストに基づいた応答生成",
        ]

        # 要件に基づいて追加の機能を追加
        if requirement.constraints:
            capabilities.append("制約条件の遵守")

        if requirement.goals:
            capabilities.append("目標指向の行動")

        return capabilities
