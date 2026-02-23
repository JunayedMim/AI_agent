from functions.get_file_content import get_file_content

content = get_file_content("calculator", "lorem.txt")
print(f"length: {len(content)}")
print(f"tail: {content[-120:]}")

assert len(content) > 10000  # because you appended the truncation message
assert "truncated at" in content

print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))



