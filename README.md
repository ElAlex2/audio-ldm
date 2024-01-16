# Text to Audio microservice

What the title says. It will create sounds based on a text description of the sound.
Quality varies depending on parameters and inference time.

# How to run
Just activate environment with conda, install requirements with pip and make a POST request using a JSON body to the endpoint /make_soundfile, with the following request:

    {
        "prompt": "A water stream",
        "negative_prompt": "Low quality",
        "cfgscale": 5,
        "seed": 56145678,
        "steps": 400,
        "length": 15,
        "file_format": "wav",
        "checkpoint": "cvssp/audioldm2"
    }

The parameters are:

- prompt: The sound you wan to recreate
- neagtive_prompt: What the sound should not be
- cfgscale: A guidance scale for the model to know how constrained it is in the creation of the sound. The higher, the more constrained. Default value is 3.
- seed: A numerical value to initialize a random generator for the sound.
- steps: The amount of inference steps for the model to render the sound. The more, the slower inference, but better quality.
- length: The amount of seconds the sound will have
- file_format: Can be "wav" or "flac" for the file to be responded
- checkpoint: There are, at the moment, three checkpoints usable with this model:

https://huggingface.co/docs/diffusers/api/pipelines/audioldm2#choosing-a-checkpoint