# Measured results

## Threshold choice (1,000 random pairs, QQP validation split, 352 duplicates)
| Threshold | Repeats caught | Wrong among hits |
|---|---|---|
| 0.80 | 74% | 33% |
| 0.90 | 41% | 22% |
| 0.95 | 20% | 12% |
| 0.96 | 15% | 9% |

Chosen threshold: 0.96, because a wrong answer costs more than a missed saving.
At 0.96 only about 50 hits occurred, so treat the 9% as roughly 10%.
Chart: threshold_chart.png

## Cache overhead
- About 25 ms per request with 100 saved questions (embedding + search).
- Break-even: with a 1,000 ms AI call, the cache pays off above a 2.5% hit rate.
- The AI delay is simulated (fake_llm), so latency savings are modelled, not measured on a real AI service.

## Complexity
- get / put (LRU): O(1) average
- expiry cleanup: O(log n) per expired entry
- similarity search: O(n) comparisons per lookup (n = saved questions)

## Known limits
- Even at 0.96, about 1 in 10 hits is wrong on this dataset.
- Search compares against every saved question, so it will not scale to millions.
- Embeddings are computed twice on a miss.
- The cache lives in memory and is emptied on restart.