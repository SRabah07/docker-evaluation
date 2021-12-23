import json

from api.utils import APIHelper

# Constants
MODEL_V2_ENDPOINT = "v2/sentiment"

MODEL_V1_ENDPOINT = "v1/sentiment"

PERMISSIONS_ENDPOINT = "permissions"


#######################
#  Authentication     #
######################


def should_be_authenticated(helper, credentials):
    result = helper.makeGetRequest(endpoint=PERMISSIONS_ENDPOINT, credentials=credentials)
    assert result['status'] == 200, 'Authentication should succeed'


def should_not_be_authenticated(helper, credentials):
    expected = {"status": "403", "message": "Forbidden"}
    result = helper.makeGetRequest(endpoint="permissions", credentials=credentials, expected=expected)
    assert result['status'] == 403, 'Authentication should failed'


def test_authentication(helper: APIHelper, credentials):
    # Should be authenticated
    credentials_ = (credentials["access_key"], credentials["secret_access_key"])
    should_be_authenticated(helper, credentials_)

    # Should be authenticated too
    credentials_ = (credentials["access_key_model_V1"], credentials["secret_access_key_model_V1"])
    should_be_authenticated(helper, credentials_)

    # Should not be authenticated
    credentials_ = (credentials["access_key_unauthorized"], credentials["secret_access_key_unauthorized"])
    should_not_be_authenticated(helper, credentials_)


#######################
#  Authorization      #
######################

def should_be_authorized(helper, endpoint, credentials):
    result = helper.makeGetRequest(endpoint=endpoint, credentials=credentials)
    assert result['status'] == 200, 'Authorization should succeed'


def should_not_be_authorized(helper, endpoint, credentials):
    expected = {"status": "403", "message": "Forbidden"}
    result = helper.makeGetRequest(endpoint=endpoint, credentials=credentials, expected=expected)
    assert result['status'] == 403, 'Authorization should failed'


def test_authorization(helper: APIHelper, credentials):
    # Should be authorized on both models versions
    credentials_ = (credentials["access_key"], credentials["secret_access_key"])
    should_be_authorized(helper, MODEL_V1_ENDPOINT, credentials_)
    should_be_authorized(helper, MODEL_V2_ENDPOINT, credentials_)

    # Should be only authorized on v1
    credentials_ = (credentials["access_key_model_V1"], credentials["secret_access_key_model_V1"])
    should_be_authorized(helper, MODEL_V1_ENDPOINT, credentials_)

    # Should not be authorized on v2
    should_not_be_authorized(helper, MODEL_V2_ENDPOINT, credentials_)


#######################
#  Prediction         #
######################

def should_predicate_sentiment(helper: APIHelper, endpoint, credentials, sentence, positive=True):
    result = helper.makeGetRequest(endpoint=endpoint, credentials=credentials, params={"sentence": sentence})
    assert result['status'] == 200, 'Should predicate'
    content = json.loads(result['content'])
    score = content['score']
    if positive:
        assert score > 0, 'Should be positive sentiment'
    else:
        assert score < 0, 'Should be negative sentiment'


def test_prediction(helper: APIHelper, credentials):
    credentials_ = (credentials["access_key"], credentials["secret_access_key"])

    # Positive sentiment
    sentence = "life is beautiful"
    should_predicate_sentiment(helper, "v1/sentiment", credentials_, sentence, True)
    should_predicate_sentiment(helper, "v2/sentiment", credentials_, sentence, True)

    # Negative prediction
    sentence = "that sucks"
    should_predicate_sentiment(helper, "v1/sentiment", credentials_, sentence, False)
    should_predicate_sentiment(helper, "v2/sentiment", credentials_, sentence, False)
