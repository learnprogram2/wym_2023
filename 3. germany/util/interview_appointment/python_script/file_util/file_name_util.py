import hashlib



def hash_verification_code(verification_code):    
    # 创建一个哈希对象    
    hasher = hashlib.sha256()    
    # 将验证码转换为字节流并更新哈希对象    
    hasher.update(verification_code.encode('utf-8'))    
    # 获取哈希结果的十六进制表示    
    hashed_code = hasher.hexdigest()    
    return hashed_code

# # 要哈希的验证码
# verification_code = "1234fdafads56"
# # 对验证码进行哈希处理
# hashed_code = hash_verification_code(verification_code)
# print("哈希后的验证码:", hashed_code)