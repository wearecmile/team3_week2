CAR_MODEL_DETAILS_MESSAGE = 'Car models details.'
CAR_BRAND_DETAILS = 'Car brand details.'
CAR_BRAND_ADDED_SUCCESSFULLY = 'Car brand details added successfully.'
PLEASE_ENTER_VALID_DATA = 'Please Add Valid Data.'
CAR_MODEL_DOES_NOT_EXISTS = 'Car model does not exists.'
CAR_BRAND_DOES_NOT_EXISTS = 'Car brand does not exists.'
CAR_MODEL_DELETED_SUCCESSFULLY = 'Car model details deleted successfully.'


def custom_response(is_error=True,message='',data={},status=''):
    return Response({"is_error": is_error, **data, 'message': message}, status=status)