/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wberger <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/07 12:17:26 by wberger           #+#    #+#             */
/*   Updated: 2022/07/07 14:43:07 by wberger          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */
#include	<unistd.h>

void	ft_write(char c)
{
	write(1, &c, 1);
}

void	ft_print_comb2(void)
{
	int	a;
	int	b;

	a = -1;
	while (++a <= 98)
	{	
		a = b;
		while (++b <= 99)
		{
			ft_write(a / 10 + '0');
			ft_write(a % 10 + '0');
			ft_write(' ');
			ft_write(b / 10 + '0');
			ft_write(b % 10 + '0');
			if (a != 98)
			{
				ft_write(',');
				ft_write(' ');
			}
		}
		b = a + 1;
	}	
}
