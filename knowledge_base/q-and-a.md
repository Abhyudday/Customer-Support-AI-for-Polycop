# Q\&A

### &#x31;**.** What is the min amount of funds I need to deposit?

* Min **deposit requirement** for the **PolyMarket's cross-chain bridge** is **$10**.
* However, **for Create copy trading, a min of $50 is required**. This is because if your capital is too low, the trades cannot be copy proportionally, which results in very poor performance.&#x20;
* After testing is complete, try to use more funds to ensure you can copy the target address’s trades proportionally. Only then can you truly match the target address’s returns.&#x20;

### 2. How to set up copy tradin&#x67;**?**

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

### 3. How to Find **smart money wallets?**

You can find **smart money wallets** through the following methods:

1. **Recommendations on X (Twitter)**.
2. **Top Holders list** under each market on the **official Polymarket website**.
3. The following third-party sites:
   * <https://polymarket.com/leaderboard>
   * <https://predicting.top/>
   * <https://polymarketanalytics.com/traders>
   * <https://app.future.fun/scouter>

To learn more, please check "[Discover Wallets](https://polycop.gitbook.io/polycop-docs/copy-trading/discover-wallets)"

### **4. What kind of smart money is worth copying?**

1. **Consistently profitable over time.**
2. **Has a large gap between profit and loss,** the total profit amount should be significantly higher than the total loss amount.
3. **Operates in markets with sufficient liquidity**, so when you copy their trades, you can enter at similar prices and with comparable position sizes.

### **5.** Why is the wallet address I exported different from the deposit address / Trade address?

We use Polymarket's official Wallet system for **gas-free** trading:

* In Polymarket, When you connect your wallet, Polymarket will based on your wallet generate a trading sub-address and a deposit sub-address. you will have a total of three different types of addresses.
  1. Trading Address

     This address is generated specifically for gasless trading. You do not need to pay gas fees when placing trades.
  2. Deposit Address

     This address is used for cross-chain deposits. You can transfer funds to it from different blockchains.
  3. Your Wallet

     This is the original wallet address you use to log in.
* You can fully view and use the wallet address generated for you by PolyCop on the Polymarket website by following these steps:
  1. On the PolyCop “wallet” page, click “Export Private Key”
  2. Import the private key into MetaMask, then open the Polymarket website and connect this wallet
  3. Go to your Polymarket personal profile page and click Copy Address to view your trading address
  4. Click the Deposit button to view your deposit address.

You can send USDC.E (Only USDC.E, Only Polygon Network) to the trading address on Polygon Network (No fee) , and send USDC or USDT to the deposit address(Low Cross-chain bridge fee / Very Low Swap fee).

### **6.** What are min trading limits on Polymarket?

For market orders, the minimum limit is $1. For limit orders, the minimum requirement is 5 shares.

> Note: You may notice transactions smaller than $1 at certain addresses. This occurs when a limit order is partially filled, resulting in a trade execution below the initial minimum threshold.

### **7.** Which bot is faster: Tokyo, California, or others?

All our bots are powered by the same high-performance engine, meaning their internal processing Copy speeds are identical.

However, the perceived response speed (latency) depends on your physical location relative to Telegram's data centers. To get the best experience:

* Pick the most responsive one: Start by testing any bot; the one that replies to you instantly is the best match for your current network.
* Switch if it feels laggy: If you experience delays in button interaction (usually due to Telegram's regional network congestion), simply switch to a different bot. All bots share the same backend data and functionality.

### **8.** Airdrop Eligibility: Am I eligible for the Polymarket $POLY airdrop?

Yes, your trading activity on PolyCop counts toward eligibility.

Since you are using the dedicated wallet address generated by Polymarket within the PolyCop platform, your on-chain interactions are fully integrated with Polymarket's ecosystem.

**Key Points on Eligibility:**

* On-chain Recording: As long as your trading activity meets Polymarket’s official airdrop criteria (such as volume, consistency, or market participation), all related data will be properly recorded and counted toward your eligibility.
* Official Builder Advantage: PolyCop is an officially recognized Polymarket Builder. This status ensures that trades routed through our platform are correctly attributed. Additionally, using a recognized Builder platform may potentially provide extra advantages or specific rewards within the ecosystem.

> \[!IMPORTANT] Disclaimer: Airdrop eligibility, rules, and distribution are entirely determined by the Polymarket team. PolyCop does not control the snapshot timing or the final allocation criteria. Please follow official Polymarket channels for the most accurate and up-to-date information regarding the $POLY token launch.

### **9.** Security Alert: Will an admin ever DM me first?

**Admins will never message you first**\
\
Scammers will impersonate admins by copying admin name and avatar.\
\
Never give them your private key or verification codes.\
They might also give you a fake bot. The only real bot is **@PolyCop\_BOT** (they may try to replace the lowercase “l” with a capital “I” or something similar)\
\
**Block and report them immediately**

### **10.** Why does my total balance change abnormally whenever I buy or sell?

Polymarket’s billing calculation can be delayed. When you sell, it records both the value of the position you closed and the amount you received after selling. The position value aggregation can also be delayed. That’s why your balance may sometimes appear inaccurate.

However, in PolyCop, the price and value of each token shown in your positions are calculated independently using real time data. The total balance, on the other hand, relies on Polymarket’s data, so it may experience delays

### **11.** Why does it fail when I click Redeem or Auto Redeem?

because there are too many users and too many requests, Polymarket has limits on Redeem feature. You need to try again later&#x20;

or check whether the market for your current token is in a dispute resolution period. Trading are not permitted while a market is in the dispute resolution phase.

### **12.** Why did the transaction result in an FAK error?

There are two main reasons for this:

1\. Your slippage tolerance is set too low while market prices are changing too rapidly.

2\. The market is nearing its close, and there are currently no limit orders available for sale.
