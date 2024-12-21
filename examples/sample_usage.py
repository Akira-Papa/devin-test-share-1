from prompt_generator.models.requirement import Requirement
from prompt_generator.core.prompt_generator import PromptGenerator


def main() -> None:
    # サンプル要件定義
    requirement = Requirement(
        title="チャットボット開発",
        description="顧客サポート用のチャットボットを開発する",
        constraints=["応答時間は2秒以内", "個人情報の取り扱いに注意"],
        goals=["顧客満足度の向上", "サポートコストの削減"],
        context="Eコマースサイトのサポート",
    )

    # プロンプト生成
    generator = PromptGenerator()
    prompt = generator.generate(requirement)

    print("\nGenerated Prompt:")
    print("===============")
    print(f"System Prompt:\n{prompt.system_prompt}\n")
    print(f"Context: {prompt.context}")
    print(f"Constraints: {prompt.constraints}")
    print(f"Capabilities: {prompt.capabilities}")
    print(f"Metadata: {prompt.metadata}")


if __name__ == "__main__":
    main()
