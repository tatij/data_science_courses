<h1>Предсказание цен недвижимости в России в 2021 году</h1>
<p>
    Автор: Сикидина Татьяна</br>
</p>
<h2>Описание проекта:</h2>
<p>
    Цель проекта - построить модель для предсказания цен недвижимости, с использованием нескольких регрессоров и выбрать наилучшую для данных целей.
</p>
<h2>Данные:</h2>
<p>
    <ul>
        <li><b>Dataset:</b> russia-real-estate-2021</li>
        <li><b>Target:</b> Стоимость(price)</li>
        <li><b>Features:</b> Дата продажи(date), этаж(level), этажность(levels), количество комнат(rooms), площадь(area), площадь кухни(kitchen_area), долгота(geo_lon), ширина(geo_lat), тип здания(object_type), регион(id_region).</li>
    </ul>
</p>
<h2>Структура проекта:</h2>
<p>Файлы:
    <ul>
        <li><b>main_recommend:</b> главный файл работы с проектом (с рекомендациями)</li>
        <li><b>loader_dataset:</b> загрузка датасета.</li>
        <li><b>mdl_analysis:</b> статистическая информация и анализ данных.</li>
        <li><b>mdl_preprocession:</b> предобработка данных.</li>
        <li><b>mdl_outliers:</b> выявление и удаление выборосов.</li>
        <li><b>mdl_regressor:</b> реализация моделей регрессоров.</li>
        <li><b>mdl_visualization:</b> визуализация графиков проекта</li>
        <li><b>main:</b> главный файл работы с проектом</li>
    </ul>
</p>
<p>Папки:
    <ul>
        <li><b>outputs:</b> все сохраненные визуализации по ходу проекта</li>
        <li><b>outputs_recommend:</b> все сохраненные визуализации по ходу проекта (с рекомендациями)</li>
    </ul>
</p>

