from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
score = scorer.score(reference_text, generated_summary)
print("ROUGE Scores:", score)
