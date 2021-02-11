data = {
    'name' : '주코박주식회사',
    'price' : {
        'open' : 1965,
        'close' : 1760,
        'high' : 2015,
        'low' : 1725
    }
}

if data['price']['close'] > data['price']['open'] :
    print('양봉입니다.')
    if data['price']['close'] < data['price']['high'] :
        print('윗꼬리가 있습니다.')
    if data['price']['open'] > data['price']['low'] :
        print('아랫꼬리가 있습니다.')
else :
    print('음봉입니다.')
    if data['price']['open'] < data['price']['high'] :
        print('윗꼬리가 있습니다.')
    if data['price']['close'] > data['price']['low'] :
        print('아랫꼬리가 있습니다.')
