七圣召唤概率论

Genius Invokatation Probability Theory
## [骰子](dice.py)
获得特定元素组合需弃牌张数的概率分布。
* 遍历状态计算理论概率，非模拟值。
* 支持不同的初始条件，代价是性能烂。

## [关键牌](keycard.py)
* 换牌黑名单机制：七圣召唤换牌时，抽不到换走牌的同名牌。
* 采取激进换牌策略时，不同牌组起手有1或2张关键牌的理论概率下次再说，模拟概率如下：
  * 2x15：61.0%
  * 2x14+2：60.5%
  * 2x13+4：60.2%
  * 2x12+6：59.8%