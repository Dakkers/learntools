# See also examples/example_track/track_meta.py for a longer, commented example
track = dict(
    author_username='alexisbcook',
    course_name='Data Visualization for All',
    course_url='https://www.kaggle.com/learn/data-viz-for-all'
)

lessons = [{'topic': topic_name} for topic_name in
            ['Introduction and Line Plots',
            'Bar Plots and Heatmaps',
            'Scatter Plots',
            'Distributions',
            'Choosing Plot Types and Custom Styles',
            'Final Project',
            'Creating Your Own Notebooks']
            ]

notebooks = [
    dict(
        filename='tut1.ipynb',
        lesson_idx=0,
        type='tutorial',
        ),
    dict(
        filename='ex1.ipynb',
        lesson_idx=0,
        type='exercise',
        scriptid=2951524
        ),
    dict(
        filename='tut2.ipynb',
        lesson_idx=1,
        type='tutorial',
        ),
    dict(
        filename='ex2.ipynb',
        lesson_idx=1,
        type='exercise',
        scriptid=2951537
        ),
    dict(
        filename='tut3.ipynb',
        lesson_idx=2,
        type='tutorial',
        ),
    dict(
        filename='ex3.ipynb',
        lesson_idx=2,
        type='exercise',
        scriptid=2951535
        ),
    dict(
        filename='tut4.ipynb',
        lesson_idx=3,
        type='tutorial',
        ),
    dict(
        filename='ex4.ipynb',
        lesson_idx=3,
        type='exercise',
        scriptid=2951534
        ),
    dict(
        filename='tut5.ipynb',
        lesson_idx=4,
        type='tutorial',
        ),
    dict(
        filename='ex5.ipynb',
        lesson_idx=4,
        type='exercise',
        scriptid=2959763
        ),
    dict(
        filename='tut6.ipynb',
        lesson_idx=5,
        type='tutorial',
        ),
    dict(
        filename='ex6.ipynb',
        lesson_idx=5,
        type='exercise',
        scriptid=2951523
        ),
    dict(
        filename='tut7.ipynb',
        lesson_idx=6,
        type='tutorial',
        ),
]

for nb in notebooks:
    nb['dataset_sources'] = ["alexisbcook/data-for-datavis"]

