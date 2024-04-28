Postman collection (Main folder - Refferal API Documentation)
```
https://www.postman.com/supply-cosmologist-43454487/workspace/github-test-tasks/collection/31564096-e1bfcd5a-7b48-4422-9e75-fada9e828367
```


### Referral API Functionality
## Installation
# 1. Clone the repository:
```
git clone https://github.com/your-repository.git
```
# 2. Install dependencies:
```
pip install -r requirements.txt
```

## Running the Server
# 1. Activate your virtual environment:
```
source /path/to/your/virtualenv/bin/activate
```
# 2. Run the Django development server:
```
python manage.py runserver
```

### API Endpoints
## Send Phone Number:
Endpoint: /api/send_phone_number/
Method: POST
Description: Send a phone number for verification and receive an authentication code.
Send Authentication Code:
Endpoint: /api/send_auth_code/
Method: POST
Description: Verify the authentication code sent to the phone number.
User Profile:
Endpoint: /api/profile/{user_id}/
Methods: GET, PATCH
Description: Get and update user profile details.

### Example Usage
# 1. Send Phone Number:
```
curl -X POST https://your-api-domain.com/api/send_phone_number/ -H "Content-Type: application/json" -d '{"phone_number": "1234567890"}'
```
# 2. Send Authentication Code:
```
curl -X POST https://your-api-domain.com/api/send_auth_code/ -H "Content-Type: application/json" -d '{"auth_code": "1234"}'
```
# 3. Get User Profile:
```
curl -X GET https://your-api-domain.com/api/profile/1/
```
# 4. Update User Profile:
```
curl -X PATCH https://your-api-domain.com/api/profile/1/ -H "Content-Type: application/json" -d '{"used_invite_code": "ABCD12"}'
```
