# Recommended Settings by Trader Type

Before you begin, remember the Golden Principles:

* The Proportionality Principle: Ensure your single trade size relative to your total balance matches the target’s. This ensures your profit margins align.
* The Anti-Drawdown Principle: Do not allow your balance to be exhausted quickly. Always leave room for market volatility.
* Strategy Alignment: Observe the target’s trade history and current positions, then select the matching profile below.

***

#### Profile 1: The Stable/Professional Trader (The "Proportional Scaler")

Characteristics: Disciplined position management, avoids "all-in" bets, consistent win rate. Best for long-term following.

Core Objective: Mirror the expert’s win-rate model while using a "safety belt" to isolate extreme risks.

* Copy Percentage: Set to 10% - 20% (adjust based on the ratio of your balance to theirs).
* Max Spend Per Trade: CRITICAL SAFETY SETTING! Set this to the maximum single loss you can tolerate (e.g., $50). This prevents you from being wiped out if the target suddenly places an oversized bet.
* Below Min Limit, Buy at Min: ON. Ensures you enter the trade at platform minimums even if the calculated copy amount is less than $1.
* Ignore Target Address Trades Under: Commonly set to $5 or $10. This must be adjusted based on your balance and the target's history to filter out "dust" trades caused by partially filled limit orders.

***

#### Profile 2: The "Whale" (The "Anti-Noise Whale")

Characteristics: Massive bankroll ($1M+), single bets in the tens of thousands, frequent order cancellations/adjustments.

Core Objective: Capture the "meat" of the move and ignore the "scraps"; prevent your balance from being drained by a whale’s infinite scaling.

* Ignore Target Address Trades Under: Recommended $500 - $1,000. Follow only significant moves and ignore "testing" trades.
* Min Per Trade: Set to $5 - $10. Ensures that once a trade is triggered, it has enough size to be meaningful.
* Max Spend Per Market: Set to 10% of your total balance. A whale can afford to lose $50k on a single market; you cannot.
* Limit Price Offset: Set to +0.02. Whales move prices quickly; bidding slightly higher ensures you get filled right behind them.

***

#### Profile 3: The High-Frequency/Algorithm (The "High-Frequency Bot")

Characteristics: Hundreds of trades daily, profits from micro-fluctuations, very short holding periods, often uses arbitrage logic.

Core Objective: Synchronize with the algorithm while using "signal filtering" to prevent fees and dust trades from draining your account.

* Copy Percentage: Use Percentage Mode based on the target's history. This ensures your position scales proportionally when the bot increases its signal strength.
* Ignore Target Address Trades Under: Recommended $5. Core "Filter" Setting. This filters out the bot's micro-adjustments or liquidity-testing trades that offer no value to you.
* Max Copy Market Number: Set to 5 - 10. Prevents the bot from spreading your capital too thin across dozens of mediocre markets.
* Take Profit: Set to a percentage (e.g., 5% - 10%). Bots usually take quick profits; you must ensure you exit automatically to lock in gains.

***

#### Profile 4: The News/Event Trader (The "News Sniper")

Characteristics: Bets on breaking news (court rulings, key tweets), reacts instantly, extreme price volatility.

Core Objective: Sacrifice price for speed; enter the position as fast as possible.

* Market Order Slippage: Set to 5% - 15%. High slippage prevents FAK (Fill-and-Kill) errors, ensuring you buy even as the price moons.
* Sell Mode: Must use Market Order. Prices crash fast once news is "priced in"; you must exit at market price to avoid being stuck.
* Below Min Limit, Buy at Min: ON. In a sniper scenario, even a $1 entry is better than missing the move.
* Max Spend Per Market: Set a Fixed Amount (e.g., $50). Snipe trades have high "go-to-zero" risks; never use a large percentage of your bankroll.

***

#### Profile 5: Low Liquidity/Price Sensitive (The "Alpha Sniper")

Characteristics: Operates in "thin" markets with low volume, extremely sensitive to entry costs.

Core Objective: Precise cost control; avoid paying unnecessary slippage to the market.

* Buy Mode: Switch to Limit Order Copy.
* Limit Price Offset: Set to 0 or +0.01. Strictly follow the target’s price or bid just $0.01 higher to "front-run" the queue.
* Limit Order Duration: Set to 120s. If not filled within 2 minutes, the price has likely moved too far; cancel to avoid buying the "top."
* Sell Mode: Use Limit Order. Attempt to sell by capturing the "spread" profit.

***

#### Profile 6: The Long-Term Visionary (The "Value Investor")

Characteristics: Focused on long-term outcomes (e.g., Presidential Elections), holds for months, ignores short-term noise.

Core Objective: Ensure entry and avoid being "shaken out" by temporary volatility.

* Limit Price Offset: Set to +0.03 or higher. Ensures you get "on board" in low-liquidity long-term markets.
* Stop Loss: Set to None or very wide (e.g., -50%). Avoid being stopped out by normal fluctuations before the final event result.
* Ignore Target Address Trades Under: Recommended $10 - $50. Follow major entries and ignore minor portfolio rebalancing.

***

#### 💡 Summary of Core Principles

1. Maintain Proportionality: Your ultimate goal is to keep your position ratio identical to the target’s. This is the only way to match their ROI percentage.
2. Establish a "Circuit Breaker": Use Max Spend Per Trade and Max Spend Per Market. Even if an expert makes a mistake or gets "tilted," your account will survive to trade another day.
