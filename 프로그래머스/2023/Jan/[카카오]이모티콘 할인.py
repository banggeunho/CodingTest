from itertools import product


def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    discount_cases = list(product(discount_rates, repeat=len(emoticons)))
    result_cases = []
    
    for discount_case in discount_cases:
        result = [0,0]
        for want_rate, money in users:
            purchase_money = 0
            for discount_rate, emoticon_price in zip(list(discount_case), emoticons):
                # 할인율이 높은게 있다면 구매
                if want_rate <= discount_rate:
                    purchase_money += emoticon_price * (100 - discount_rate) // 100
                    
            # 이모티콘 플러스 구독 / 구매 취소
            if purchase_money >= money:
                result[0] += 1
            # 이모티콘 구매가격 더하기
            else:
                result[1] += purchase_money
        # 결과 저장
        result_cases.append(result)
        
    # 정렬
    result_cases.sort(key=lambda x:(-x[0], -x[1]))
    return result_cases[0]