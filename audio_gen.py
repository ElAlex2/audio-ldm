import scipy
import torch
from diffusers import AudioLDM2Pipeline
from model import RequestTxt2Wav
import gc

def make_audio_sample(request_data: RequestTxt2Wav):

    repo_id = request_data.checkpoint
    pipe = AudioLDM2Pipeline.from_pretrained(repo_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")

    prompt_embeds, attention_mask, generated_prompt_embeds = pipe.encode_prompt(
        prompt=request_data.prompt,
        negative_prompt=request_data.negative_prompt,
        device="cuda",
        do_classifier_free_guidance=False,
        num_waveforms_per_prompt=1
    )

    generator = torch.Generator("cuda").manual_seed(request_data.seed)

    audio = pipe(
        prompt_embeds=prompt_embeds,    
        attention_mask=attention_mask,
        generated_prompt_embeds=generated_prompt_embeds,
        num_inference_steps=request_data.steps,
        audio_length_in_s=(request_data.length * 2),
        guidance_scale=request_data.cfgscale,
        generator=generator
    ).audios[0]

    # Go forth and be free
    prompt_embeds = None
    generated_prompt_embeds = None
    torch.cuda.empty_cache()
    torch.cuda.ipc_collect()
    gc.collect()    
    
    return audio