# Copy Trading Parameter Guide

#### 1. Copy Percentage / Fixed Amount ($)

Determines how much you invest per trade relative to the target.

* Percentage Mode (e.g., 10%): If the target buys $100 worth of shares, you buy $10.
* Fixed Amount Mode (e.g., $50): You always buy $50 regardless of the target's trade size.
* How to Switch: Type the number with or without the `%` symbol when prompted.

#### 2. Limit Price Offset

* Description: Sets a price offset for limit orders so your purchase price is slightly higher or lower than the target’s, increasing fulfillment likelihood.
* Input Requirements: Can be negative, range `-0.99` \~ `0.99`, or enter `reset` to clear.
* Recommended Setting: Enter `0.02` to buy at $0.02 above the target price for better execution.

#### 3. Limit Order Duration

* Description: Sets the lifespan of a limit order.
* Input Requirements: Seconds (positive integer), minimum `90` seconds, no upper limit.
* Default Behavior: Orders will not cancel by default. If set, they auto-cancel upon expiration.

#### 4. Market Order Slippage

* Description: Represents the maximum price deviation you are willing to accept. The system always prioritizes the best available market price.
* Note on FAK Logic: If slippage is too low, you may see error `400 no orders found to match with FAK order`. Polymarket uses Fill-and-Kill (FAK) logic; if liquidity isn't found within your slippage range, the order is partially filled or killed entirely to prevent unfavorable prices.

#### 5. Below min limit, buy at min

* Description: If enabled, when the calculated copy amount is lower than the platform's minimum requirement, the trade executes at the minimum.
* Platform Minimums: $1 for market orders; 5 shares for limit orders.
* 💡 Pro Tip: Best used in combination with Item #6.

#### 6. Ignore Target Address Trades Under

* Description: Sets a minimum trade amount to ignore from target addresses.
* Input Requirements: `0` \~ `9,999,999`, or `reset`.
* 💡 Anti-Noise Strategy: \* Setup: Set `Ignore` to $10–$50 and Enable `Below min limit`.
  * Result: This filters out "dust" trades (noise). When the target makes a "real" trade (e.g., $100), even if your 1% copy ratio equals $1, the bot will ensure you enter the position at the platform minimum.

#### 7. Max Price & Min Price

* Max Price: Highest price to copy buy (`0.01` \~ `0.99`). Trades above this are ignored.
* Min Price: Lowest price to copy buy (`0.01` \~ `0.99`). Trades below this are ignored.

#### 8. Stop Loss % / Price

* Input: Percentage (`0.1%` \~ `100%`) or Fixed Price (`0.01` \~ `0.99`).
* Execution Logic: All Stop Loss orders use Market Orders. When prices move sharply, market orders may experience price slippage.

#### 9. Take Profit % / Price

* Input: Percentage (`0.1%` \~ `100%`) or Fixed Price (`0.01` \~ `0.99`).
* Execution Logic (PM Constraints):
  * For orders ≥ 5 shares: The system places a Limit Order immediately to lock in gains.
  * For orders < 5 shares: The system uses Market Orders. Note that market orders may experience slippage during volatility.

#### 10. Min Per Trade

* Description: Minimum amount per copy trade.
* Input: `1` \~ `9,999,999`, `reset`, or `-` for no limit.
* Logic: If the calculated copy amount is lower than this value, it executes at this minimum.

#### 11. Max Spend Per Trade

* Description: Maximum amount per copy trade.
* Input: `1` \~ `9,999,999`, `reset`, or `-` for no limit.
* Logic: If the calculated amount exceeds this, the trade is capped at this value.

#### 12. Max Spend Per Yes/No (Asset Limit)

* Description: Maximum USD amount allocated to a single Asset (token).
* Calculation Includes: Successfully executed orders + Open limit orders (from this bot) + The current pending trade.
* Note: This represents your cumulative exposure per specific asset.

#### 13. Max Spend Per Market (Market Limit)

* Description: Maximum capital allocated to a single Market / ConditionId.
* Logic: Sums the total USD spent on both Yes and No options within the same market to prevent over-concentration in a single event.

#### 14. Total Spend Limit (Trader Limit)

* Description: Total amount to spend across all assets.
* Logic: If total exposure exceeds this, copying stops. It automatically resumes after you sell or claim positions and exposure drops below the limit.

#### 15. Max Copy Market Number

* Description: Maximum number of distinct markets (`ConditionIds`) you can hold simultaneously.
* Purpose: A count-based limit to ensure portfolio diversification.

#### 16. Copy Buy / Copy Sell Toggles

* Disable Copy Buy: Stops replicating buys; continues replicating sells.
* Disable Copy Sell: Stops replicating sells; continues replicating buys.
* Disable Both: Pauses all copy-trading activity.

#### 17. Sell: Market Order / Sell: Limit Order

* Market Order: Allows slippage configuration.
* Limit Order: Allows Price Offset and Expiration configuration.
* 🚨 \[!CAUTION] TP/SL Compatibility: If you switch Sell mode to Limit Order, TP/SL will no longer function. TP/SL is only compatible with Market Orders because Polymarket does not allow two concurrent limit orders on the same position.

#### 18. Max 5/15min Market start Time

* What it is: The "Sniper" or early-entry mode.
* What it does: If you set this to `60s`, your bot will **ONLY** copy trades made within the **first 60 seconds** after the market opens. Any trades made by the target wallet after the first 60 seconds will be ignored.

#### 19. Max 5/15min Market end Time

* What it is: The "Last-Minute" or late-entry mode.
* What it does: If you set this to `60s`, your bot will **ONLY** copy trades made when there are **less than 60 seconds left** before the market closes. Any trades made earlier in the market will be ignored.
