from vk_api import vk 
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.upload import VkUpload
import vk_api

# ������� ��� ������ ������� � �������������
def start_conversation(user_id: int) -> None:
    print("Starting conversation with user", user_id)

    # �������� ��������������� ��������� � ���������� ��� ������ ����
    message = ("������!\n� ���, ������� ������� ��� ����� ���������� �����.\n"
               "�������� ���, ������� �� �����:")

    keyboard = create_start_conversation_keyboard()
    # �������� ��������� � �����������
    write_msg(user_id=user_id, message=message, keyboard=keyboard)

    # ��������� ��������� ������������ � "�������� ������ ����"
    db.set_state_user(user_id, "waiting_for_gender")
    print("DB State: ", db.get_state_user(user_id), "user_id:", user_id)
    print("Sent gender selection keyboard to user", user_id)

def process_gender(user_id: int, gender: str) -> None:
    print("Processing gender selection for user", user_id)

    if gender.lower() == "�������" or gender.lower() == "�������":
        print('gender: ', gender, 'user_id: ', user_id)
        db.set_search(self_id=user_id, sex=gender)

        # �������� ���������� � �������� ��� ������ ��������
        keyboard = create_action_keyboard()

        write_msg(user_id, "��� �� ������ �������?",
                  keyboard=keyboard
                  )
        db.set_state_user(user_id, "waiting_for_action")
        print("Sent action selection keyboard to user", user_id)
    else:
        write_msg(
                user_id=user_id,
                message="�� ������ ������ ������. "
                        "����������, �������� ��� �� ������."
        )
        print("Sent invalid gender response message to user", user_id)
def get_user_city(user_id: int) -> str | None:
    try:
        response = vk.users.get(user_ids=user_id, fields='city')
        city_info = response[0]['city']
        if city_info:
            city = city_info['title']
            return city
        else:
            return None
    except Exception as e:
        print("Error getting user city:", str(e))
        return None

