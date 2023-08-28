import os
def write_file_to_folder(filename, file_bytes, folder_path):    
    if file_bytes == '':
        return
    # Create the folder if it doesn't exist    
    if not os.path.exists(folder_path):        
        os.makedirs(folder_path)    
    
    # Construct the file path    
    file_path = os.path.join(folder_path, filename)    
    
    # Write the file to the folder    
    with open(file_path, 'wb') as file:        
        file.write(file_bytes)    
        # print(f"File '{filename}' has been written to '{folder_path}'.")
        
        
# Example usagefilename = "example.txt"file_bytes = b"This is an example file."folder_path = "path/to/folder"write_file_to_folder(filename, file_bytes, folder_path)


def write_to_html(content):    
    with open("output.html", "w", encoding="utf-8") as file:        
        file.write(content)

# 调用submit_form函数获取响应内容
#response_content = submit_form(captchaText, cookies)
# 将响应内容写入HTML文件
# write_to_html(response_content.decode("utf-8"))
