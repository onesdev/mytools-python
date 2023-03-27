"""
模拟计算复利增长下的总资产
"""


def cal_asset(annual_income, deposit, annual_income_increase, return_on_investment, total_years, this_year):
    """
    Calculate the total asset after x years.
    :param annual_income: 家庭年收入
    :param deposit: 当前存款
    :param annual_income_increase: 年收入增长，单位万元
    :param return_on_investment: 长期年化投资回报率，单位%
    :param total_years: 需要计算的总年数
    :param this_years 当前年数
    :return: total asset：总资产
    """
    if this_year <= total_years:
        asset = deposit * (1 + return_on_investment) + annual_income
        print(f'In {str(this_year)}th year, the total asset is {str(asset)} wan-yuan.')

        cal_asset(
            annual_income + annual_income_increase,
            asset,
            annual_income_increase,
            return_on_investment,
            total_years,
            this_year + 1
            )
    else:
        print(f'After {str(total_years)} years, the total asset is {str(deposit)} wan-yuan.')
        return    
    
if __name__ == '__main__':
    cal_asset(
        30,  # 年收入30万元
        200,  # 当前存款200万元
        1,  # 年收入增长1万元
        0.1,   # 长期年化投资回报率10%
        30,  # 需要计算的总年数
        1
    )


