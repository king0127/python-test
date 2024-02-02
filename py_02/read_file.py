

subject_vals = []

# with open('./test.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         # print(line)
#         line_str = line.split(',')
#         subject_vals.append(line_str[1])
# print(subject_vals)
# print(len(subject_vals))

# with open('.text.txt', 'w') as wf:
#     for i in subject_vals:
#         wf.write(i)
#         wf.write(',')
    # wf.writelines(subject_vals)


subject_dict = {}
review_subject = {}

def read_review_subject(review_subject):
    with open('D:\wangshuai95012_58016\Desktop\dev备份0906\module_subject_relation.sql', 'r') as fs:
        data = fs.readlines()
        for d in data:
            d_fix = d.split('VALUES (')[1]
            res_data = d_fix.split(',')
            sub = res_data[1].strip()
            dict_key = res_data[0].strip()
            review_subject[dict_key] = sub
    return review_subject



def read_subject(subject_dict):
    with open(r'D:\wangshuai95012_58016\Desktop\dev备份0906\subject.sql', 'r', encoding='gb18030', errors='ignore') as fs2:
        lines = fs2.readlines()
        for line in lines:
            line_data = line.split('VALUES (')[1]
            res_data = line_data.split(',')
            subject_id = res_data[0].strip()
            subject_name = res_data[1].strip()
            subject_dict[subject_id] = subject_name
    return subject_dict


# def check_subject(review_subject, subject_dict):





read_review_subject(review_subject)
read_subject(subject_dict)

print(review_subject, subject_dict)


# print(review_subject.values())
print(len(subject_dict.values()))