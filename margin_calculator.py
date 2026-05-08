import json

def calculate_promotion_margin(base_cost, daily_price, platform_threshold, platform_discount, shop_threshold, shop_discount):
    """
    计算电商大促期间，叠加多层优惠后的最终单品到手价与实际毛利率。
    这可以作为 Agent 的核心 Function Tool。
    """
    
    # 1. 模拟理想凑单逻辑：假设消费者正好凑满平台满减门槛
    # 计算该单品需要分摊的平台优惠比例 (例如满300减50，折扣率就是 50/300)
    platform_discount_ratio = platform_discount / platform_threshold
    item_platform_discount = daily_price * platform_discount_ratio

    # 2. 叠加店铺专属优惠券
    # 判断该单品的日常价是否直接满足了店铺券门槛
    if daily_price >= shop_threshold:
        item_shop_discount = shop_discount
    else:
        # 如果单价未达门槛，现实中通常需要消费者拼单，这里为简化按保守策略计为0，或按比例分摊
        item_shop_discount = 0 

    # 3. 计算最终到手价
    final_price = daily_price - item_platform_discount - item_shop_discount

    # 4. 测算实际利润与毛利率
    gross_profit = final_price - base_cost
    margin_rate = (gross_profit / final_price) * 100 if final_price > 0 else 0

    return {
        "daily_price": daily_price,
        "final_price": round(final_price, 2),
        "gross_profit": round(gross_profit, 2),
        "margin_rate": f"{round(margin_rate, 2)}%"
    }

# --- 测试用例 ---
# 假设你正在主推一款复古渔夫鞋，出厂材质与物流总成本为 145 元。
# 日常标价定为 289 元。
# 参加平台跨店每满 300 减 50 活动，店铺自己再发一张满 200 减 30 的优惠券。

result = calculate_promotion_margin(
    base_cost=145,
    daily_price=289,
    platform_threshold=300,
    platform_discount=50,
    shop_threshold=200,
    shop_discount=30
)

print("Agent 利润测算执行结果:")
print(json.dumps(result, ensure_ascii=False, indent=2))