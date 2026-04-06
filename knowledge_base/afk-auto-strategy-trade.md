# AFK Auto Strategy Trade

## 🤖 PolyCop AFK Auto Trade Guide

Welcome to the AFK (Away From Keyboard) Automated Strategy Engine, built by PolyCop specifically for Polymarket's 15-minute high-frequency prediction markets.

In extremely volatile prediction markets, the AFK engine allows you to preset multi-dimensional trigger conditions. It enables the bot to monitor order books and spot data streams in milliseconds on the cloud, executing precise "snipes" on your behalf.

#### 🌟 Core Features: Multi-Threading & Dynamic UI

* Parallel & Interference-Free: You can create multiple identical strategies simultaneously (default tags are `AFK 1`, `AFK 2`, etc.). Each strategy runs in an independent sandbox on the cloud without interfering with others. You can set up exclusive monitoring programs for different time frames or varying levels of aggression.
* Immersive Dynamic Interaction: PolyCop features a minimalist control panel design. Simply click the settings buttons below the message, input your parameters, and the strategy status text above will update instantly in real-time. What you see is what you get—say goodbye to tedious command inputs.

***

### ⚙️ Strategy Parameters & Configuration Guide

To get the bot working, you need to configure the following parameters by clicking the buttons below the panel. When you click a button, PolyCop will prompt you with the following inputs:

#### 1. Triggers

These three conditions must be met simultaneously for the bot to instantly trigger a buy action.

* ⏱ Time Range

  Set the valid monitoring time window (calculated from the opening of each 15-minute round).

  > Bot Prompt:
  >
  > Please enter the time in the format: 00:00, 14:99
  >
  > PolyCop will monitor the Up price and BTC change during this time range after each round starts. Once the conditions are met, it will immediately place a limit order:
* 📈 UP Price Range

  The UP share price range you are willing to enter, preventing you from chasing highs during extreme volatility.

  > Bot Prompt:
  >
  > Please enter the Up price in the format: 0.01, 0.99
  >
  > PolyCop will monitor the Up price and BTC change within the time range you set after each round starts. Once the conditions are met, it will immediately place a limit order:
* 🪙 BTC Price Change

  The absolute change in spot BTC price compared to the opening of the current market round.

  > Bot Prompt:
  >
  > Please enter the BTC price change in the format: -100, 100, 9999 *(Supports negative numbers for drops, positive for pumps)*

#### 2. Trade Settings

Once the above conditions collide successfully, PolyCop will execute your order based on the following parameters:

* 🔄 Trade Direction: The panel provides a one-click toggle button to seamlessly switch between `Buy UP` and `Buy DOWN`.
* 💲 Limit Price & TTL (Time To Live): Set the specific price of your limit order and how long the order survives on the order book. If it times out without being filled, PolyCop will actively cancel the order to prevent you from becoming a passive bag-holder.
* 💰 Single Trade Buy Amount:

  > Bot Prompt:
  >
  > Please enter Single trade buy amount, Min $5:
* 🔁 Execution Rounds:

  > Bot Prompt:
  >
  > Please enter the number of rounds to buy, with 1 round every 15 minutes:

#### 3. Position Management (TP/SL)

After a successful fill, the system will automatically place a take-profit or stop-loss limit order for you. You can set this by specific price or percentage of cost; the system will automatically cap the maximum order price at 0.99.

* 🏆 TP (Take Profit):

  > Bot Prompt:
  >
  > Enter a percentage (0.1%–100%) or a price (0.01–0.99). If you enter a percentage, the system will set a take-profit limit order based on the purchase price, with a maximum price of 0.99:
* 🛑 SL (Stop Loss):

  > Bot Prompt:
  >
  > Enter a percentage (0.1%–100%) or a price (0.01–0.99). If you enter a percentage, the system will set a stop-loss limit order based on the purchase price, with a maximum price of 0.99:
  >
  > PolyCop will monitor the Up price and BTC change within the time range you set after each round starts. Once the conditions are met, it will immediately place a limit order:

***

### 📚 Combat Templates: One-Click Copy Pro Strategies

Not sure how to set it up? You can refer to the following battle-tested parameters and fine-tune them according to your risk appetite:

#### 🎯 Template 1: The Theta Harvester (Late-Stage Arbitrage)

Strategy Logic: Extremely high win rate. In the last 2 minutes, if BTC still maintains an absolute advantage (e.g., up by $40), buy decisively to capture the final time decay profit.

* Time Range: `13:00, 14:55`
* UP Price: `0.70, 0.90`
* BTC Change: `40, 9999`
* Buy Params: `🟢 Buy UP` | Limit `0.90`
* TP/SL: None (Hold directly until the 15-minute round ends, waiting for automatic settlement to get 1 USDC)

#### 🚀 Template 2: The Breakout Scalper

Strategy Logic: Capture trends brought by sudden news or large spot market dumps at the opening. Snatch cheap shares before prediction market market makers adjust their prices.

* Time Range: `00:30, 01:00`
* UP Price: `0.01, 0.89`
* BTC Change: 5`0, 9999`
* Buy Params: `🟢 Buy UP` | Market Buy
* TP/SL: NO

#### 💣 Template 3: The Flash Crash Rebound

Strategy Logic: Extreme market conditions hit mid-round, and panic selling drives prices absurdly low. Buy on the left side with an extremely small position to bet on a high-return mean reversion bounce.

* Time Range: `04:00, 11:00`
* UP Price: `0.01, 0.15`
* BTC Change: `-200, -10`
* Buy Params: `🟢 Buy UP` | Amount `$5` (Lottery play, control position size strictly)
* TP/SL: TP `0.45` / SL None (Run if it doubles, treat a wipeout like a losing lottery ticket)

It's just a data point:

> We backtested an Opening Range Breakout strategy adapted for Polymarket's BTC 5-minute markets. Across 4,389 trades, here's what we found.
>
> The strategy: When BTC moves past the price targets and the price is below the accuracy %, buy.
>
> \- BTC moves $10 in first minute: 57% accuracy that side wins &#x20;
>
> \- BTC moves $10–25: 68% accuracy &#x20;
>
> \- BTC moves $50–100: 76% accuracy &#x20;
>
> \- BTC moves $100+: 99% accuracy &#x20;
>
> The first 60 seconds of BTC price action predicts the 5-minute resolution quite accurately.
>
> If BTC moves up from the strike in the first minute → buy UP &#x20;
>
> If BTC moves down → buy DOWN&#x20;
>
> Hold to resolution.
>
> That's it. No indicators. No ML. Just momentum.
>
> When the market shows its hand early, it usually plays through.
>
> If you want to backtest your own strategies, PolyBackTest has subsecond historical data going back a month. --- Poly backtest
