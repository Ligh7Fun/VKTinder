import vk_api
import random

# ����������� ����
vk_session = vk_api.VkApi(token='���_�����')
vk = vk_session.get_api()

# ������� ��� ������ ������������� �� �������� ����������
def search_users(age_from, age_to, sex, city, status):
    users = vk.users.search(
        age_from=age_from,
        age_to=age_to,
        sex=sex,
        city=city,
        status=status,
        count=10  # ���������� ������������� ��� ������
    )
    return users['items']

# ������� ��� ��������� ���-3 ���������� ���������� ������������
def get_top_photos(user_id):
    photos = vk.photos.get(owner_id=user_id, album_id='profile', extended=1)
    photos = sorted(photos['items'], key=lambda x: x['likes']['count'], reverse=True)
    top_photos = photos[:3]
    return top_photos

# �������� ���� ����
def main():
    while True:
        # �������� ��������� �� ������������ (�������� ��������, ���, �����, �������� ���������)
        age_from = int(input("������� ����������� �������: "))
        age_to = int(input("������� ������������ �������: "))
        sex = int(input("������� ��� (1 - �������, 2 - �������): "))
        city = int(input("������� ID ������: "))
        status = int(input("������� �������� ��������� (1 - �� �����/�� �������, 2 - � �������� ������): "))

        # ����� �������������
        users = search_users(age_from, age_to, sex, city, status)

        # �������� ���-3 ���������� �������������
        for user in users:
            user_id = user['id']
            top_photos = get_top_photos(user_id)
            vk.messages.send(
                user_id=user_id,
                message="��� ���-3 ���������� ���������� � ������ �������:",
                attachment=",".join([f'photo{photo["owner_id"]}_{photo["id"]}' for photo in top_photos])
            )

if __name__ == '__main__':
    main()
