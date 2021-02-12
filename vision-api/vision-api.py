from google.cloud import vision_v1
import os
import proto
import json

project_id = "bustling-victor-301010"
topic_id = "test-topic"


def sample_batch_annotate_files(storage_uri):
    mime_type = "application/pdf"

    client = vision_v1.ImageAnnotatorClient()

    gcs_source = {"uri": storage_uri}
    input_config = {"gcs_source": gcs_source, "mime_type": mime_type}
    features = [
        {"type_": vision_v1.Feature.Type.LABEL_DETECTION},
        {"type_": vision_v1.Feature.Type.TEXT_DETECTION},
        {"type_": vision_v1.Feature.Type.IMAGE_PROPERTIES},
        {"type_": vision_v1.Feature.Type.CROP_HINTS},
        {"type_": vision_v1.Feature.Type.DOCUMENT_TEXT_DETECTION},
        {"type_": vision_v1.Feature.Type.WEB_DETECTION}
    ]
    pages = [1]
    requests = [{"input_config": input_config, "features": features, "pages": pages}]

    response = client.batch_annotate_files(requests=requests)
    json_dict = proto.Message.to_dict(response)
    with open('example-response.json', 'w') as fp:
        json.dump(json_dict, fp)


if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../keys/simonetestingproject.json"

    sample_batch_annotate_files("gs://simonetestingproject-test-bucket/test-vision.pdf")
