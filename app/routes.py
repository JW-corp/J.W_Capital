from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# 투자 데이터 (콤마 없는 순수 숫자)
FUND_DATA = {
    'initial_investment': 2000000,
    'current_value': 2102542
}


def format_currency(value):
    # 숫자를 콤마가 포함된 문자열로 변환
    return format(value, ',')


def calculate_return_rate():
    initial = float(FUND_DATA['initial_investment'])
    current = float(FUND_DATA['current_value'])

    return_rate = ((current - initial) / initial) * 100
    return f"{'+' if return_rate > 0 else ''}{return_rate:.2f}"


@main.route('/')
def home():
    return render_template('index.html',
                           initial_investment=format_currency(FUND_DATA['initial_investment']),
                           current_value=format_currency(FUND_DATA['current_value']),
                           return_rate=calculate_return_rate())