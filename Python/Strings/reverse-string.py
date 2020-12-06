def reverse(str):
    left = 0
    right = len(str)-1

    while left <= right:
        # swap
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1
    return str

def test():
    assert reverse('harshith') == 'htihsrah
    
