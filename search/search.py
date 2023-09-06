from vk_api import vk_user  

def process_search(user_id: int) -> None:
    write_msg(user_id, "�������� ������...")
    data = db.get_search(user_id)
    count = 50
    sex = '1' if data['sex'].lower() == '�������' else '2'
    print('city id: ', get_city_id(data['city']))

    search_results = vk_user.users.search(count=count,
                                          country=1,  # ������
                                          sex=sex,
                                          city=get_city_id(data['city']),
                                          age_from=str(data['age_from']),
                                          age_to=str(data['age_to']),
                                          has_photo='1',
                                          status='6',
                                          sort=1,
                                          fields="city, bdate, sex"
                                          )
    print(len(search_results['items']))
    print()
    print(search_results['items'])
    print("***" * 20)

    # ��������� ���������� ������ � ���� ������
    db.set_search(self_id=user_id, results=None)
    db.set_search(self_id=user_id, results=search_results['items'])

    # ������������� ��������� ������������ ��� ������ ��������
    db.set_state_user(self_id=user_id, state="showing_profiles")
    # ������������� ��������� ������ �� 0
    if db.get_search_index(self_id=user_id) == 0:
        db.set_search_index(self_id=user_id, new_index=0)

    # ���������� ������ �������
    display_profile(user_id=user_id)
