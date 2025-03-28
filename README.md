<h2>Курс «Data Science: машинное обучение и нейронные сети»</h2>
<p>
    Автор: Сикидина Татьяна</br>
    Репозиторий содержит решения домашних работ курса по Data Science
</p>
<h2>Содержание</h2>
<p>
    <ul>
        <li><a href="#hm1">Домашняя работа №1</a></li>
        <li><a href="#hm2">Домашняя работа №2</a></li>
        <li><a href="#hm3">Домашняя работа №3</a></li>
        <li><a href="#hm4">Домашняя работа №4</a></li>
        <li><a href="#hm5">Домашняя работа №5</a></li>
    </ul>
</p>
<h2 id='hm1'>Домашняя работа №1</h2>
<h3>Описание:</h3>
<p>
    Работа с различными типами данных (списки, кортежи, словари, множество) и функциями.
</p>
<h2 id='hm2'>Домашняя работа №2</h2>
<p>
    <h4>Описане:</h4>
    <p>Работа с загрузкой датасетов из различных источников. Работа с визуализацией данных с помощью гистаграмм, линейных графиков и диаграмм рассеяния. Работа с данными датасета. Анализ данных по стоимости и свойствам различных ноутбуков. Проверка на связь между стоимостью и различными свойствами ноутбуков.</p>
    <h4>Задание:</h4>
    <p>
        <ol>
            <li>Выбрать датасет исходя из интересов</li>
            <li>Создать модуль data_loader для загрузки данных (CSV, JSON, API)</li>
            <li>Создать методы для добавления и удаления различных типов визуализации (гистаграмма, линейный график, диаграмма рассеяния)</li>
            <li>Реализовать метод для подсчета пустых или пропущенных значений</li>            
        </ol>
    </p>
    <h4>Струкрура проекта:</h4>
    <p>
        Проект состоит из нескольких этапов, каждый из которых выполняется отдельным скриптом. Ниже описано, что делает каждый файл и в каком порядке их нужно запускать.
    </p>
    <h4>Реализация:</h4>
    <p>
        <ol>
            <li>Загрузка данных
                <ul>
                    <li>Файл: 'data_loader.py'</li>
                    <li>Описание: Загружает данные из файла 'dataset_laptop.csv'.</li>
                    <li>Запуск:
                        <p>
                            '''bash
                            python data_loader.py
                            '''
                        </p>                    
                    </li>
                </ul>
            </li>
            <li>Анализ данных (EDA)
                <ul>
                    <li>Файл: 'module_for_laptop.py'</li>
                    <li>Описание: Проводит исследовательский анализ данных (EDA), включая:
                        <ul>
                            <li>Проверку структуры данных.</li>
                            <li>Распределение целевой переменной 'Brand'</li>
                            <li>Проверку на пропущенные значения</li>
                            <li>Построение корреляционной матрицы</li>
                        </ul>                    
                    </li>
                    <li>Запуск:
                        <p>
                            '''bash
                            python module_for_laptop.py
                            '''
                        </p>  
                    </li>
                </ul>            
            </li>
            <li>Визуализация
                <ul>
                    <li>Файл: 'graph.py'</li>
                    <li>Описание: Визуализация анализа данных, включая:
                        <ul>
                            <li>Столбчатая гистаграмма частоты повторения Processor ноутубков</li>
                            <li>Столбчатая гистаграмма частоты повторения GPU ноутубков</li>
                            <li>Линейный график зависимотсти стоимости от ширины экрана ноутбуков</li>
                            <li>Диаграмма рассеяния зависимостей стоимости и операционной системы ноутбуков</li>
                        </ul>
                    </li>
                    <li>Запуск:
                        <p>
                            '''bash
                            python graph.py
                            '''
                        </p>  
                    </li>
                </ul>
            </li>
        </ol>
    </p>
    <h4>Зависимости</h4>
    <p>
        Для запуска проекта необходимо установить следующие библиотеки:
        <ul>
            <li>matplotlib</li>
            <li>numpy</li>
            <li>pandas</li>
            <li>seaborn</li>
            <li>sys</li>
        </ul>
    </p>
</p>
<h2 id='hm3'>Домашняя работа №3</h2>
<h3>Описание:</h3>
<p>
    Анализ данных датасета с пассажирами Титаника.
    Знакомство с базами данных, инструментами для работы с запросами и агрегатными функциями. Визуализация данных с помощью библиотеки Matplotlib.
</p>
<h2 id='hm4'>Домашняя работа №4</h2>
<h3>Описание:</h3>
<p>
    Предсказание наличия сердечных заболеваний.
    Знакомство с классификаторами и реализация моделей обучения. 
</p>
<h2 id='hm5'>Домашняя работа №5</h2>
<h3>Описание:</h3>
<p>
    Предсказание цен недвижимости в России в 2021 году.
    Знакомство с регрессорами и реализация моделей обучения. 
</p>


