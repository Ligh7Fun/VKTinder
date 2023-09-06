import re
from db import db 

from database.db import Database 

# ������� ��� ��������� ������ ��������
def process_action(user_id: int, action: str) -> None:
    print("Processing action selection for user", user_id)
    print("Received action:", action)
    # �������� ���� � ����� �� ������ ������
    action_text = re.sub(r'^\d+\.\s*', '', action)

    if action_text.lower() == "������ �� ������ �� �������":
        user_city = get_user_city(user_id)
        if user_city:
            db.set_state_user(user_id, "waiting_for_age_from")
            db.set_search(self_id=user_id, city=user_city)
            print('city: ', user_city, 'user: ', user_id)
            # ��������� ��������� ��� ����� ��������
            city_message = f"����� �� ������ �������: {user_city}."
            confirm_keyboard = create_confirm_city_keyboard(user_city)
            write_msg(user_id, city_message, keyboard=confirm_keyboard)
            return
        else:
            db.set_state_user(user_id, "waiting_for_city")
            action_keyboard = create_action_keyboard()
            write_msg(user_id, "����� �� ������ � ����� �������.\n"
                               "������� ����� �������:",
                      keyboard=action_keyboard
                      )
    else:
        db.set_state_user(user_id, "waiting_for_city")
        write_msg(user_id, "������� ����� ��� ������:")
    print("Sent city input prompt to user", user_id) 
    
def process_confirm_change(user_id: int, choice: str) -> None:
    if choice.lower() == "��":
        db.set_state_user(user_id, "waiting_for_city")
        # ��������� � �������� ����� ������
        action_keyboard = create_action_keyboard()
        write_msg(user_id, "������� ����� ��� ������:",
                  keyboard=action_keyboard
                  )
    elif choice.lower() == "���":
        db.set_state_user(user_id, "waiting_for_action")
        # ��������� � ������ ��������
        action_keyboard = create_action_keyboard()
        write_msg(user_id, "��� �� ������ �������?",
                  keyboard=action_keyboard
                  )
    else:
        write_msg(user_id, "����������, �������� \"��\" ��� \"���\".")