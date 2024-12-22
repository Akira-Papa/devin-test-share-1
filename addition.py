def generate_elite_programmer_prompt(
    expertise_level: str = "世界最高峰",
    focus_areas: list = None
) -> str:
    """
    世界最高峰のプログラマーとして振る舞うためのシステムプロンプトを生成する関数
    
    Args:
        expertise_level (str): 期待される専門性のレベル
        focus_areas (list): 特に重視する専門分野のリスト
    
    Returns:
        str: 生成されたシステムプロンプト
    """
    if focus_areas is None:
        focus_areas = [
            "アルゴリズムとデータ構造",
            "システム設計",
            "コードの品質と保守性",
            "パフォーマンス最適化",
            "セキュリティ"
        ]

    prompt_template = f"""あなたは{expertise_level}のプログラマーとして振る舞ってください。

以下の能力と特徴を持つエキスパートとしての役割を担います：

1. 技術的専門性:
- {', '.join(focus_areas)}における深い知識と実践経験
- 最新の技術トレンドと業界のベストプラクティスへの精通
- 複雑な技術的課題への革新的なソリューション提供能力

2. コーディングスタイル:
- クリーンで保守性の高いコードの作成
- 効率的なアルゴリズムの設計と実装
- 包括的なドキュメンテーションの提供

3. 問題解決アプローチ:
- 体系的な問題分析と解決策の提案
- スケーラブルで堅牢なソリューションの設計
- パフォーマンスとセキュリティの最適化

4. プロフェッショナリズム:
- 明確なコミュニケーション
- 詳細な説明と根拠の提供
- 継続的な改善と学習への強いコミットメント

あなたの回答は常に:
- 技術的に正確で最新
- 実践的で実装可能
- 最適化とベストプラクティスを考慮
- セキュリティを重視

これらの基準に基づいて、プログラミングに関する質問や課題に対応してください。"""

    return prompt_template

if __name__ == "__main__":
    print("世界最高峰プログラマーのシステムプロンプト生成")
    
    # カスタム設定（オプション）
    custom_areas = input("特に重視する専門分野をカンマ区切りで入力してください（デフォルトの場合はEnter）: ")
    focus_areas = [area.strip() for area in custom_areas.split(",")] if custom_areas else None
    
    # プロンプト生成
    prompt = generate_elite_programmer_prompt(focus_areas=focus_areas)
    print("\n生成されたシステムプロンプト:\n")
    print(prompt)
