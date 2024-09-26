import requests
import json


def prompting(body, prompt):
    """
    a function that sends the prompts to a llm

    Parameters
    - function parameter
    - object:
    {
        "model_endpoint": string,
        "token": string,
        "tags": {
            "prefix": ,
            "suffix":
        },
        #tags are optional
        "prompt": string
    }

    Return
    - string
    - OR returns an error in case the URL is wrong

    """

    try:
        # importing data from body as json and storing in the appropriate variables
        url = body.get("model_endpoint")
        token = body.get("token")
        payload = json.dumps({
            "inputs": prompt
        })
        headers = {
            'content-type': body.get("Content-Type"),
            'Authorization': token
        }
        if len(prompt) == 0:
            return prompt
        response = requests.request("POST", url,headers=headers,
                                    data=payload)
        if response.status_code in [200, 201]:
            # content = response.json()[0]("generated_text")
            # content = response.json()[0]["generated_text"]
            return (response.json())["generated_text"]
        else:
            return {"error": response.text}
    except Exception as e:
        return {"error": str(e)}



# print(prompting(body, "Which year did brooklyn 99 air"))


