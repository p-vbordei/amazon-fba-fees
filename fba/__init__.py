from .united_states import UnitedStates

US = UnitedStates()

def Fees(marketplace="US"):
    """Factory function returns class corresponding to country """

    factory = {"US": UnitedStates}

    return factory[marketplace]()
