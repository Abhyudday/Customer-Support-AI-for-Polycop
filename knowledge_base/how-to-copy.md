# How to Copy

### Creating a Copy Task

Setting up a copy task is simple, but understanding the settings is crucial for profitability and risk management.

#### Step 1: Add a Target **Address**

Simply paste the **Wallet Address** or the **Polymarket Profile Link** of the trader you want to follow into the bot chat.

The bot will generate a control panel for this specific target.

#### Step 2: Configuration (Important!)

Before activating the task, you need to configure how you want to follow this trader. Here is a breakdown of every setting:

**1. Copy Percentage / Fixed Amount ($)**

This determines how much you invest per trade compared to the target.

* **Percentage Mode (e.g., 10%):** If the target buys $100 worth of shares, you will buy $10.
* **Fixed Amount Mode (e.g., $50):** Regardless of how much the target buys, you will always buy $50 worth.
  * *To switch modes, simply type the number with or without the `%` symbol when prompted.*
  * *Recommendation:* Use percentage mode and make sure you have enough funds to copy the target address’s trades proportionally.

**2. Max Spend Per Yes/No**

**Risk Management.** This is the maximum amount you are willing to hold for **a single specific outcome (Token)**.

* *Example:* If set to $50, and the target keeps buying "Trump to Win", the bot will stop copying once your exposure on "Trump to Win" hits $50.

**Total Spend Limit.** This is the max amount you are willing to hold for **all market**.

**3. Below Min Limit, Buy at Min (❌ / ✅)**

**⚠️ Crucial Setting for Small Accounts.** Polymarket has a minimum bet size (usually around $1).

* **Disabled (❌):** If your calculated copy amount is less than $1 (e.g., $0.50), the bot will **SKIP** the trade.
* **Enabled (✅):** If your calculated amount is less than $1, the bot will **round up** and force a buy of the minimum amount (approx. $1).
  * *Recommendation:* Enable this if you are copying with a small percentage (e.g., <5%) to avoid missing trades. It’s recommended to also set “Ignore Target Wallet Trades Under” to $5.

**4. Ignore Target Wallet Trades Under ($)**

**"Dust Filter".** This helps you avoid copying insignificant test trades.

* If the target buys only $0.10 or $1 worth of shares to "test" the market, you might not want to waste **resources** copying such insignificant trades.
* *Recommendation:* Set this to **$5**. The bot will ignore any trade where the target spends less than $5.

**5. Limit Price Offset & Duration**

Advanced settings for execution price.

* **Market Order (Default):** Buys immediately at the current available price.
* **Limit Price Offset:** Allows you to set a limit order slightly better or worse than the target's entry price to manage slippage.

#### Step 3: Activate the Task

Once configured, click the **"Active"** button (it should turn Green ✅).

* **Note:** You must have enough **Available USDC** in your PolyCop wallet. Funds tied up in other positions cannot be used for new copy trades.

#### Pro Tips for Strategy

1. **The "Arbitrage" Setup:** If you are following a high-frequency arbitrage bot, they often make small trades.
   * **Recommended:** Enable `Below Min Limit` ✅.
   * **Warning:** This consumes more capital as it rounds up every small trade to $1.
2. **The "Whale" Setup:** If you are following a whale who bets $10,000 at a time.
   * **Recommended:** Use `Copy Percentage` (e.g., 1%) and set a `Max Copy Amount` to protect your wallet from sudden massive bets.

### How to set up copy tradin&#x67;**?**

Two principles for **setting copy trading** parameters:

&#x20;1\. **Match the position ratio of the target address**.\
&#x20;2\. Don’t spend all your funds too quickly, to avoid small fluctuations wiping out your principal.\
With small capital, results rely more on luck. Having **sufficient capital** and following these principles leads to more reasonable and stable settings.

You can set up copy trading by following the steps below. If you stick to these, you’ll generally avoid problems:

1. Choose the target address

   First, confirm which address you want to copy. Try to choose addresses that are not high frequency arbitrage and have a stable trading logic.
2. Choose the copy mode

   There are two common options:

   Fixed amount mode: copy each trade with a fixed amount, suitable for testing.

   Percentage mode: copy based on the target address’s position ratio, which is better for matching long term returns.
3. Set the copy ratio or amount

   In percentage mode, make sure your capital is sufficient. Otherwise, the calculated amount may fall below the minimum order requirement.
4. Control how fast your funds are used

   Do not spend all your funds too quickly. Leave room for follow up buys and market fluctuations to avoid small movements wiping out your principal.
5. Check minimum order requirements

   Both market orders and limit orders have minimum requirements. Orders below the minimum will fail to copy.
6. Confirm sell rules

   Check whether Sell uses a market order or a limit order.

   Note that TP and SL only work when Sell uses a market order.
7. Check switch status

   Make sure copy trading is enabled and not restricted by conditions such as max price or max spend.

In short:

Test first, then add more funds. Copy by ratio and always leave enough buffer.
