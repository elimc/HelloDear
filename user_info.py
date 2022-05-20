def get_scammer_info(tg, scammer_id=None):
    """
    Grab the scammer's info.
    """
    result_of_get_user = tg.get_user(scammer_id)
    # Wait for the result with blocking `wait` method.
    result_of_get_user.wait()
    if result_of_get_user.error:
        print('Did not get scammer info')
        return False
    else:
        scammer_info = result_of_get_user.update
        scammer_id = scammer_info['id']
        # Print scammer ID to CLI if successful.
        print(f'Scammer ID: {scammer_id}')
        return scammer_id


def get_my_info(tg):
    """
    Grab my info.
    """
    result_of_get_me = tg.get_me()  # Preload my info.
    result_of_get_me.wait()  # Wait for the result with blocking `wait` method.
    if result_of_get_me.error:
        print('Did not get my info')
        return False
    else:
        personal_id = result_of_get_me.update
        my_id = personal_id['id']
        print(f'My ID: {my_id}')  # Print my ID to CLI if successful.
        return my_id
