import hashlib

username = "GOUGH"
hash_result = hashlib.sha256(username.encode()).hexdigest()

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = hash_result[4] + hash_result[5] + hash_result[3] + hash_result[6] + hash_result[2] + hash_result[7] + hash_result[1] + hash_result[8]
key_part_static2_trial = "}"

flag = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(flag)
