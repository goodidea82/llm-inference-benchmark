from optimum.nvidia.pipelines import pipeline
import time

pipe = pipeline('text-generation', 'mlabonne/NeuralDaredevil-7B')
for i in range(5):
    start_time = time.time()
    pipe("Describe a real-world application of AI in sustainable energy.", max_new_tokens=128)
    print(f"Generation time: {time.time() - start_time}s")