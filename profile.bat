REM cProfiler + KCacheGrind
REM python -m cProfile -o profile.out demo.py
REM pyprof2calltree -i profile.out -o profile.calltree
REM F:\setup\qcachegrind074-x86\qcachegrind.exe profile.calltree

REM Line_profiler
REM kernprof -l -v demo.py
REM python -m line_profiler demo.py.lprof

REM Memory_profiler
python -m memory_profiler demo.py
mprof list
mprof clean
REM pip install matplotlib
mprof run demo.py
mprof plot