import click
from random import randint
from constants import receipts_data, emojies_data
from typing import Callable


from pizza_class import Pizza


@click.group()
def cli():
    '''main function'''
    pass


def log(text: str) -> Callable:
    '''make logging for module's functions'''
    def decorator(func: Callable) -> Callable:
        def wrapper(pizza):
            cooking_time = randint(1, 10)
            print(text.format(pizza.name, pizza.size, cooking_time))

        return wrapper

    return decorator


@log('\U0001F373 Приготовили {} {} за {}c!')
def bake(pizza) -> None:
    '''coock pizza'''
    pass


@log('\U0001F9BC Доставили {} {} за {}c!')
def delivery_pizza(pizza) -> None:
    '''delivery pizza'''
    pass


@log('\U0001F5FF Забрали {} {} за {}c!')
def pickup(pizza) -> None:
    '''pickup pizza'''
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', default='L', nargs=1)
def order(pizza: str, size: str, delivery: bool) -> None:
    '''make and delivery'''
    pizza_instance = Pizza(pizza, size)
    bake(pizza_instance)
    if delivery:
        delivery_pizza(pizza_instance)
    else:
        pickup(pizza_instance)


@cli.command()
def menu() -> None:
    '''print menu'''
    for pizza_name, ingredients in receipts_data.items():
        print(f'— {pizza_name} {emojies_data[pizza_name]} : {", ".join(ingredients)}')


if __name__ == '__main__':
    cli()
