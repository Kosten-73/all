import re
def has_valid_characters(s):
    allowed_characters = re.compile(r'^[a-z0-9._]+$')

    return bool(allowed_characters.match(s))
def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        stri = ''
        for _ in range(n):
            stri += input()

        result_list = stri.split('files')
        k = 0
        for now in result_list:
            now_str = str(now)
            if now_str.find('.') != -1:
                if str(now_str.split('.')).find('hack') != -1:
                    for top in str(now.strip().split("\"")).split('dir'):
                        if top.find('.hack') != -1:
                            for pot in top.split(','):
                                if pot.find('.') != -1:
                                    k += 1
                                    # print(pot)
                                elif pot[2:-1] != 'dir' and pot[2:-1] != 'files' and pot[2:-1] != 'folders' and has_valid_characters(pot[2:-1]):
                                    k += 1
                                    # print(pot)
        print(k)

if __name__ == "__main__":
    main()
