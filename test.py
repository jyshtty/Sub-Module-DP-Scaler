# # # write your code here...
# # import requests
# # url =  "https://assets.scaler.com/assets/scaler/webp/focus-image-banner-10f2febd2e4988deb4c5a5cb5f5b9f806e9c52ece336dde51dfee7c8661364f6.webp.gz"
# # image = request.get(url)
#
# def foo():
#     offset = 0
#     ans = []
#     for i in range(5):
#         offset = (i * 5)
#         temp = []
#         for j in range(5):
#             temp.append(offset + j)
#         ans.append(temp)
#     return ans
#
# def rotate(mat):0
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if j<i:
#                 mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
#     print(mat)
#     for i in range(len(mat)):
#         mat[i] = mat[i][::-1]
#
#     return mat
#
# mat = foo()
# print(mat)
# print(rotate(mat))
#
#
#
#

def deco(func):
    def wrapper():
        print("Good morning")
        func()
        print("Good evening")
    return wrapper

@deco
def foo():
    print("Ajay Shetty")

foo()





