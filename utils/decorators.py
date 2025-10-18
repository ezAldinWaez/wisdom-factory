"""Decorators"""

import functools
import time
from typing import Callable


def persist(func: Callable) -> Callable:
    """Persist function state across calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = f"{func.__name__}_{hash(str(args) + str(kwargs))}"
        print(f"🔄 PERSIST: Checking cache for {func.__name__} with key: {cache_key[:20]}...")
        
        if hasattr(wrapper, '_cache') and cache_key in wrapper._cache:
            cached_result = wrapper._cache[cache_key]
            print(f"✅ PERSIST: Cache HIT! Returning cached result: {cached_result}")
            return cached_result

        print(f"❌ PERSIST: Cache MISS. Executing {func.__name__}...")
        result = func(*args, **kwargs)
        
        if not hasattr(wrapper, '_cache'):
            wrapper._cache = {}
            print(f"📦 PERSIST: Initializing cache for {func.__name__}")
        
        wrapper._cache[cache_key] = result
        print(f"💾 PERSIST: Cached result for {func.__name__}: {result}")
        return result
    return wrapper


def iterate(func: Callable) -> Callable:
    """Iterate function until success"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        max_attempts = 100
        attempt = 0
        start_time = time.time()
        print(f"🔄 ITERATE: Starting {func.__name__} with max {max_attempts} attempts")
        
        while attempt < max_attempts:
            attempt += 1
            print(f"🔁 ITERATE: Attempt {attempt}/{max_attempts} for {func.__name__}")
            
            try:
                result = func(*args, **kwargs)
                if result:
                    elapsed = time.time() - start_time
                    print(f"✅ ITERATE: SUCCESS! {func.__name__} succeeded on attempt {attempt} after {elapsed:.2f}s")
                    return result
                else:
                    print(f"❌ ITERATE: Attempt {attempt} failed (falsy result), retrying...")
                    time.sleep(0.1)
            except Exception as e:
                print(f"💥 ITERATE: Attempt {attempt} raised {type(e).__name__}: {e}")
                if attempt >= max_attempts:
                    print(f"🚫 ITERATE: Max attempts reached for {func.__name__}")
                    raise e
                print(f"⏳ ITERATE: Waiting before retry...")
                time.sleep(0.1)
        
        total_time = time.time() - start_time
        error_msg = f"Function {func.__name__} failed after {max_attempts} attempts in {total_time:.2f}s"
        print(f"🚫 ITERATE: {error_msg}")
        raise RuntimeError(error_msg)
    return wrapper


def learn(func: Callable) -> Callable:
    """Learn from function execution patterns"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, '_learnings'):
            wrapper._learnings = []
            print(f"🧠 LEARN: Initializing learning system for {func.__name__}")
        
        learning_count = len(wrapper._learnings)
        print(f"📚 LEARN: Executing {func.__name__} (learning session #{learning_count + 1})")
        
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            
            learning_entry = {
                'success': True,
                'execution_time': execution_time,
                'args': args,
                'kwargs': kwargs
            }
            wrapper._learnings.append(learning_entry)
            
            # Calculate learning stats
            successes = sum(1 for l in wrapper._learnings if l['success'])
            avg_time = sum(l['execution_time'] for l in wrapper._learnings) / len(wrapper._learnings)
            
            print(f"✅ LEARN: SUCCESS! {func.__name__} completed in {execution_time:.3f}s")
            print(f"📊 LEARN: Stats - Success rate: {successes}/{len(wrapper._learnings)} ({successes/len(wrapper._learnings)*100:.1f}%), Avg time: {avg_time:.3f}s")
            
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            
            learning_entry = {
                'success': False,
                'execution_time': execution_time,
                'error': str(e),
                'args': args,
                'kwargs': kwargs
            }
            wrapper._learnings.append(learning_entry)
            
            # Calculate failure stats
            failures = sum(1 for l in wrapper._learnings if not l['success'])
            print(f"❌ LEARN: FAILURE! {func.__name__} failed after {execution_time:.3f}s with {type(e).__name__}")
            print(f"📊 LEARN: Failure count: {failures}/{len(wrapper._learnings)} ({failures/len(wrapper._learnings)*100:.1f}%)")
            
            raise
    return wrapper


def debug(func: Callable) -> Callable:
    """Debug function execution with detailed logging"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        print(f"🐛 DEBUG [{timestamp}]: ===== ENTERING {func.__name__} =====")
        print(f"🐛 DEBUG: Function: {func.__module__}.{func.__name__}")
        print(f"🐛 DEBUG: Args: {args}")
        print(f"🐛 DEBUG: Kwargs: {kwargs}")
        print(f"🐛 DEBUG: Args types: {[type(arg).__name__ for arg in args]}")
        
        start_time = time.time()
        try:
            print(f"🐛 DEBUG: Executing {func.__name__}...")
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            
            print(f"✅ DEBUG: {func.__name__} completed successfully in {execution_time:.4f}s")
            print(f"🐛 DEBUG: Return value: {result}")
            print(f"🐛 DEBUG: Return type: {type(result).__name__}")
            print(f"🐛 DEBUG [{timestamp}]: ===== EXITING {func.__name__} =====")
            
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            print(f"💥 DEBUG: {func.__name__} FAILED after {execution_time:.4f}s")
            print(f"🐛 DEBUG: Exception type: {type(e).__name__}")
            print(f"🐛 DEBUG: Exception message: {str(e)}")
            print(f"🐛 DEBUG: Exception args: {e.args}")
            print(f"🐛 DEBUG [{timestamp}]: ===== EXITING {func.__name__} WITH ERROR =====")
            raise
    return wrapper
