import neuralfoil as nf
import aerosandbox as asb
import time
import torch

torch.set_num_threads(1)
def test_basic_functionality():
    initial_time = time.time()
    nf.get_aero_from_airfoil(asb.Airfoil("naca4412"), alpha=5, Re=1e6, model_size="xxxlarge")#, device="cuda",)
    print("Time taken: ", time.time() - initial_time)   

if __name__ == "__main__":
    # pytest.main()
    test_basic_functionality()
